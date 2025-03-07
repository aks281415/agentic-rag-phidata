from phi.utils.text_splitter import TextSplitter

def split_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200):
    splitter = TextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)
