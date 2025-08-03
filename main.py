from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (safe for development only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


l={
    "1":"Apple",
    "2":"Banana",
    "3":"Cherry",
    "4":"Date",
}

@app.get("/")
def read_root():
    return l

@app.get("/messafe")
def read_root():
    return {"Hello": "Bro"}


@app.post("/postList/")
async def read_root(request: Request):
    item = await request.json()
    print(item)

    if "item" in item and item["item"] not in l.values():
        id = str(len(l) + 1)
        l[id] = item["item"]
        print(f'Added: {item["item"]}')
    else:
        print(" or already exists in the list. Not adding.")

    return l