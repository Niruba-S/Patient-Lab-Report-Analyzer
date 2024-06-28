
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from openai import OpenAI 
import fitz
import PIL.Image
import io
import base64
import os

class pdf_extractor():
    def __init__(self,pdf_path) -> None:
        self.pdf=pdf_path
    def extract(self):
        pdf=PdfReader(self.pdf)
        raw_text=""
        for i,page in enumerate(pdf.pages):
            content = page.extract_text()
            if content:
                raw_text+=content
                raw_text+=content
        text_splitter=CharacterTextSplitter(
            separator='\n',
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        text=text_splitter.split_text(raw_text)
        return text


class display:
    def __init__(self, pdf,key):
        self.key = key
        self.pdf = pdf
    
    def summary(self,text):
        client = OpenAI(api_key=self.key)
        message = [
                    {"role": "system", "content": "You are a data analyst."},
                    {"role": "user", "content": f"Analyze the following data and provide 3-4 line of summary: {text}"}
                ]


        response =  client.chat.completions.create(
                    model="gpt-4o",
                messages=message)
            
        return response.choices[0].message.content



    def analyze(self,im_text):
        client = OpenAI(api_key=self.key)
        extractor =pdf_extractor(self.pdf)
        text = extractor.extract()
        text+=im_text
        if len(text)==0:
            return ""
        else:
            message = [
                {"role": "system", "content": "You are a medical report analyzer."},
                {"role": "user", "content": f" Analyze the following medical reports extracted from the PDF and information extracted from images. Merge the information and provide a detailed, structured analysis without adding a summary: {text}"}
            ]
            ]
            response =  client.chat.completions.create(
                    model="gpt-4o",
                messages=message)
            text=response.choices[0].message.content
            out="output.pdf"
            # self.text_to_pdf(text,"output.pdf")
            return text
    def get_openai_response(self,info,query):
        client = OpenAI(api_key=self.key)
        message = [
        {"role": "system", "content": "You are a data analyst."},
        {"role": "user", "content": f"Analyze the following information and answer the query: {info}\n\nUser Query: {query}"}
    ]
  
        response = client.chat.completions.create(
            model="gpt-4o", 
            messages=message
        )
        return response.choices[0].message.content
    def clear_output_folder(self,output_folder):

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        else:
            for file_name in os.listdir(output_folder):
                file_path = os.path.join(output_folder, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
    def extract_image(self):
        output_folder="output_folder"
        self.clear_output_folder(output_folder)
        pdf = fitz.open(self.pdf)
        image_paths = []

        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            images = page.get_images()

            for index, image in enumerate(images):
                base_img = pdf.extract_image(image[0])
                image_data = base_img["image"]
                img = PIL.Image.open(io.BytesIO(image_data))

                extension = base_img["ext"]
                image_filename = f"image{page_num + 1}_{index + 1}.{extension}"
                image_path = os.path.join(output_folder, image_filename)
                img.save(open(image_path, "wb"))

                image_paths.append(image_path)
        return image_paths
    
    def encode_image_to_base64(self,image_path):
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    def message(self):
        images=self.extract_image()
        
        messages=[]
        for image in images:
            base64_image=self.encode_image_to_base64(image_path=image)
            mess={
                "role": "user",
                "content": [
                    {"type": "text", "text": "your are given image of medical reports analyze and extarct detailed info"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
            messages.append(mess)
        return messages
        
    def request(self):
        client = OpenAI(api_key=self.key)
        messages=self.message()
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages)
        return (response.choices[0].message.content)


        


        


