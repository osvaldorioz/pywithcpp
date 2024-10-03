from fastapi import FastAPI
import bindings  # Importa la biblioteca compilada con Pybind11

app = FastAPI()

@app.get("/cpp")
def read_root():
    result = bindings.add(5, 3)  # Llama a la función C++
    return {"message": f"5 + 3 = {result}"}
