from extract import extract_text_from_images
from parallel_chain import parallel_chain
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq

image_files = ["page1.png", "page2.png", "page3.png"]
ocr_texts = extract_text_from_images(image_files)

results = []
for text in ocr_texts:
    output = parallel_chain.invoke({"text": text})
    results.append(output)

for i, (text, res) in enumerate(zip(ocr_texts, results)):
    print(f"\nPage {i+1}")
    print("Summary:", res['summary'])
    print("Entities:", res['entities'])

# Optional interaction
model = ChatGroq(model="llama3-8b-8192")
chat_history = []

combined = ""
for i, (text, res) in enumerate(zip(ocr_texts, results)):
    combined += f"\nPage {i+1}\n"
    combined += f"Text:\n{text}\n"
    combined += f"Summary:\n{res['summary']}\n"
    combined += f"Entities:\n{res['entities']}\n"

chat_history.append(SystemMessage(content="Use the following context to answer questions:\n" + combined))

while True:
    q = input("Ask something (or type 'exit'): ")
    if q.lower().strip() == "exit":
        break

    chat_history.append(HumanMessage(content=q))
    reply = model.invoke(chat_history)
    print("Reply:", reply.content)
    chat_history.append(AIMessage(content=reply.content))