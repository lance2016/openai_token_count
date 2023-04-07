from fastapi import FastAPI
import tiktoken
from loguru import logger

app = FastAPI()


@app.post('/count/')
def get_word_count(params: dict) -> dict:
    try:
        prompt = params.get("prompt", "")
        encoding_name = params.get("encoding_name", "p50k_base")
        return_detail = params.get("return_detail", False)
        if len(prompt) == 0:
            return FailResponse("prompt 不能为空")
        encoding = tiktoken.get_encoding(encoding_name)
        logger.info(prompt)
        """Returns the number of tokens in a text string."""
        # 将 text 进行编码
        token_integers = encoding.encode(prompt)
        num_tokens = len(token_integers)
        token_bytes = [encoding.decode_single_token_bytes(token) for token in token_integers]
        tokens_list = [tb.decode("utf-8", 'replace') for tb in token_bytes]
        if return_detail:
            return_dict = {
                "tokens_num": num_tokens,
                "tokens": tokens_list,
                "token_integers": token_integers,
            }
            return SuccessResponse(return_dict)
    except Exception as e:
        logger.error(e)
        return FailResponse(e)
    return SuccessResponse(f"tokens_num: {num_tokens}")


class Response:
    def __init__(self, text: str, code: int, message: str, success: bool):
        self.text = text
        self.code = code
        self.message = message
        self.success = success


# SuccessResponse继承Response
class SuccessResponse(Response):
    def __init__(self, text: str, message: str = "success"):
        super().__init__(text, 200, message, success=True)


# FailResponse继承Response
class FailResponse(Response):
    def __init__(self, text: str, message: str = "fail"):
        super().__init__(text, 500, message, success=False)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, host="localhost", reload=True)

