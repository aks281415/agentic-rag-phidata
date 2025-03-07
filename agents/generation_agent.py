from phi.agent import Agent
from phi.model.openai import OpenAIChat
from config.settings import settings
from schemas.models import GeneratedResponse

class GenerationAgent:
    def __init__(self):
        self.agent = Agent(
            model=OpenAIChat(model=settings.main_model),
            description="Generates the final response based on the augmented prompt.",
            instructions=[
                "Use the augmented prompt to generate a comprehensive response.",
                "Ensure the response is accurate, relevant, and well-structured.",
                "Cite sources from the retrieved information when appropriate.",
                "Provide a concise summary at the end of the response."
            ],
            response_model=GeneratedResponse,
            structured_outputs=True,
            read_chat_history = True
        )

    def generate(self, augmented_prompt: str) -> GeneratedResponse:
        try:
            response = self.agent.run(f"Generate a response for: {augmented_prompt}")

            # ✅ Directly return `response.content` since it is already a `GeneratedResponse`
            if isinstance(response.content, GeneratedResponse):
                return response.content

            # ✅ Convert dictionary response (if needed)
            if isinstance(response.content, dict):
                return GeneratedResponse(
                    response=response.content.get("response", "No response found."),
                    summary=response.content.get("summary", "No summary available."),
                    sources=response.content.get("sources", [])
                )

            # ✅ Return a fallback in case of unexpected structure
            return GeneratedResponse(
                response="Unexpected response format.",
                summary="Error handling response."
            )

        except Exception as e:
            print(f"Generation error: {str(e)}")
            return GeneratedResponse(
                response="An error occurred during response generation.",
                summary="Error in generation process."
            )
