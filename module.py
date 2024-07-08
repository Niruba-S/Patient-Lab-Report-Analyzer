
# from langchain.text_splitter import CharacterTextSplitter
# from PyPDF2 import PdfReader
# from openai import OpenAI 
# import fitz
# import PIL.Image
# import io
# import base64
# import os

# class pdf_extractor():
#     def __init__(self,pdf_path) -> None:
#         self.pdf=pdf_path
#     def extract(self):
#         pdf=PdfReader(self.pdf)
#         raw_text=""
#         for i,page in enumerate(pdf.pages):
#             content = page.extract_text()
#             if content:
#                 raw_text+=content
#                 raw_text+=content
#         text_splitter=CharacterTextSplitter(
#             separator='\n',
#             chunk_size=800,
#             chunk_overlap=200,
#             length_function=len,
#         )
#         text=text_splitter.split_text(raw_text)
#         return text


# class display:
#     def __init__(self, pdf,key):
#         self.key = key
#         self.pdf = pdf
    
#     def summary(self,text):
#         client = OpenAI(api_key=self.key)
#         message = [
#                     {"role": "system", "content": "You are a data analyst."},
#                     {"role": "user", "content": f"Analyze the following data and provide 3-4 line of summary: {text}"}
#                 ]


#         response =  client.chat.completions.create(
#                     model="gpt-4o",
#                 messages=message)
            
#         return response.choices[0].message.content



#     def analyze(self,im_text):
#         client = OpenAI(api_key=self.key)
#         extractor =pdf_extractor(self.pdf)
#         text = extractor.extract()
#         text+=im_text
#         if len(text)==0:
#             return ""
#         else:
#             message = [
#                 {"role": "system", "content": "You are a medical report analyzer."},
#                 {"role": "user", "content": f" Analyze the following medical reports extracted from the PDF and information extracted from images. Merge the information and provide a detailed, structured analysis without adding a summary: {text}"}

#             ]
#             response =  client.chat.completions.create(
#                     model="gpt-4o",
#                 messages=message)
#             text=response.choices[0].message.content
#             out="output.pdf"
#             # self.text_to_pdf(text,"output.pdf")
#             return text
#     def get_openai_response(self,info,query):
#         client = OpenAI(api_key=self.key)
#         message = [
#         {"role": "system", "content": "You are a data analyst."},
#         {"role": "user", "content": f"Analyze the following information and answer the query and answer the query only given from the given infomation: {info}\n\nUser Query: {query}"}
#     ]
  
#         response = client.chat.completions.create(
#             model="gpt-4o", 
#             messages=message
#         )
#         return response.choices[0].message.content
#     def clear_output_folder(self,output_folder):

#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)
#         else:
#             for file_name in os.listdir(output_folder):
#                 file_path = os.path.join(output_folder, file_name)
#                 try:
#                     if os.path.isfile(file_path):
#                         os.remove(file_path)
#                 except Exception as e:
#                     print(f"Error deleting {file_path}: {e}")
#     def extract_image(self):
#         output_folder="output_folder"
#         self.clear_output_folder(output_folder)
#         pdf = fitz.open(self.pdf)
#         image_paths = []

#         for page_num in range(len(pdf)):
#             page = pdf.load_page(page_num)
#             images = page.get_images()

#             for index, image in enumerate(images):
#                 base_img = pdf.extract_image(image[0])
#                 image_data = base_img["image"]
#                 img = PIL.Image.open(io.BytesIO(image_data))

#                 extension = base_img["ext"]
#                 image_filename = f"image{page_num + 1}_{index + 1}.{extension}"
#                 image_path = os.path.join(output_folder, image_filename)
#                 img.save(open(image_path, "wb"))

#                 image_paths.append(image_path)
#         return image_paths
    
#     def encode_image_to_base64(self,image_path):
#         with open(image_path, 'rb') as image_file:
#             return base64.b64encode(image_file.read()).decode('utf-8')
#     def message(self):
#         images=self.extract_image()
        
#         messages=[]
#         for image in images:
#             base64_image=self.encode_image_to_base64(image_path=image)
#             mess={
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": "your are given image of medical reports analyze and extarct detailed info"},
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image}"
#                         }
#                     }
#                 ]
#             }
#             messages.append(mess)
#         return messages
        
#     def request(self):
#         client = OpenAI(api_key=self.key)
#         messages=self.message()
#         response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=messages)
#         return (response.choices[0].message.content)




# from langchain.text_splitter import CharacterTextSplitter
# from PyPDF2 import PdfReader
# from openai import OpenAI 
# import fitz
# import PIL.Image
# import io
# import base64
# import os

# class pdf_extractor():
#     def __init__(self,pdf_path) -> None:
#         self.pdf=pdf_path
#     def extract(self):
#         pdf=PdfReader(self.pdf)
#         raw_text=""
#         for i,page in enumerate(pdf.pages):
#             content = page.extract_text()
#             if content:
#                 raw_text+=content
#                 raw_text+=content
#         text_splitter=CharacterTextSplitter(
#             separator='\n',
#             chunk_size=800,
#             chunk_overlap=200,
#             length_function=len,
#         )
#         text=text_splitter.split_text(raw_text)
#         return text

# def extract_image(pdf):
#     output_folder="output_folder"
#     if not os.path.exists(output_folder):
#             os.makedirs(output_folder)
#     else:
#         for file_name in os.listdir(output_folder):
#             file_path = os.path.join(output_folder, file_name)
#             try:
#                 if os.path.isfile(file_path):
#                     os.remove(file_path)
#             except Exception as e:
#                 print(f"Error deleting {file_path}: {e}")

#     pdf = fitz.open(pdf)
#     image_paths = []
#     print("Inside messages")
#     for page_num in range(len(pdf)):
#         page = pdf.load_page(page_num)
#         images = page.get_images()

#         for index, image in enumerate(images):
#             base_img = pdf.extract_image(image[0])
#             image_data = base_img["image"]
#             img = PIL.Image.open(io.BytesIO(image_data))

#             extension = base_img["ext"]
#             image_filename = f"image{page_num + 1}_{index + 1}.{extension}"
#             image_path = os.path.join(output_folder, image_filename)
#             img.save(open(image_path, "wb"))
#             print(image_path)
#             image_paths.append(image_path)
#     return image_paths
# class display:
#     def __init__(self, pdf,key):
#         self.key = key
#         self.pdf = pdf
    
#     def summary(self,text):
#         client = OpenAI(api_key=self.key)
#         message = [
#                     {"role": "system", "content": "You are a data analyst."},
#                     {"role": "user", "content": f"Analyze the following data and provide 3-4 line of summary: {text}"}
#                 ]


#         response =  client.chat.completions.create(
#                     model="gpt-4o",
#                 messages=message)
            
#         return response.choices[0].message.content



#     def analyze(self,im_text):
#         client = OpenAI(api_key=self.key)
#         extractor =pdf_extractor(self.pdf)
#         text = extractor.extract()
#         text+=im_text
#         if len(text)==0:
#             return ""
#         else:
#             message = [
#                 {"role": "system", "content": "You are a medical report analyzer."},
#                 {"role": "user", "content": f" Analyze the following medical reports extracted from the PDF and information extracted from images. Merge the information and provide a detailed, structured analysis without adding a summary: {text}"}

#             ]
#             response =  client.chat.completions.create(
#                     model="gpt-4o",
#                 messages=message)
#             text=response.choices[0].message.content
#             out="output.pdf"
#             # self.text_to_pdf(text,"output.pdf")
#             return text
#     def get_openai_response(self,info,query):
#         client = OpenAI(api_key=self.key)
#         message = [
#         {"role": "system", "content": "You are a quetion answer bot."},
#         {"role": "user", "content": f"Analyze the following information and answer the query and answer the query only given from the given infomation and should know the basic meaning of medical term in the report: {info}\n\nUser Query: {query}"}
#     ]
  
#         response = client.chat.completions.create(
#             model="gpt-4o", 
#             messages=message
#         )
#         return response.choices[0].message.content
   
    
#     def encode_image_to_base64(self,image_path):
#         with open(image_path, 'rb') as image_file:
#             return base64.b64encode(image_file.read()).decode('utf-8')
#     def message(self):
#         print("123")
#         images=extract_image(self.pdf)
#         print("456")
#         messages=[]
#         for image in images:
#             base64_image=self.encode_image_to_base64(image_path=image)
#             mess={
#                 "role": "user",
#                 "content": [
#                    {"type": "text", "text": "your are given images of medical reports analyze and extarct detailed info without leaving any image and any information"},
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image}"
#                         }
#                     }
#                 ]
#             }
#             messages.append(mess)
#         return messages
        
#     def request(self):
#         client = OpenAI(api_key=self.key)
#         messages=self.message()
#         response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=messages)
#         return (response.choices[0].message.content)



from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader

import fitz
import PIL.Image
import io
import base64
from openai import OpenAI 
import os
import boto3
import time
import uuid
import os
from dotenv import load_dotenv

load_dotenv()


def analyze_text_from_pdf_s3(pdf_path):
    # Generate a random file name
    object_name = str(uuid.uuid4()) + ".pdf"
    
    # S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('aws_access_key'),
        aws_secret_access_key=os.getenv('aws_secret_key'),
        region_name=os.getenv('region_name')
    )
    bucket_name=os.getenv('bucket_name')
    # Upload PDF to S3
    s3.upload_file(pdf_path, bucket_name, object_name)
    print(f"Uploaded {pdf_path} to s3://{bucket_name}/{object_name}")

    # Amazon Textract client
    textract = boto3.client(
        'textract',
        aws_access_key_id=os.getenv('aws_access_key'),
        aws_secret_access_key=os.getenv('aws_secret_key'),
        region_name=os.getenv('region_name')
    )

    # Start the asynchronous analysis of the document
    response = textract.start_document_analysis(
        DocumentLocation={'S3Object': {'Bucket': bucket_name, 'Name': object_name}},
        FeatureTypes=['FORMS', 'TABLES']
    )

    # Get the JobId from the response
    job_id = response['JobId']

    # Poll the job status
    status = ""
    while status not in ["SUCCEEDED", "FAILED"]:
        response = textract.get_document_analysis(JobId=job_id)
        status = response["JobStatus"]
        print(f"Job status: {status}")
        if status in ["SUCCEEDED", "FAILED"]:
            break
        time.sleep(5)

    if status == "SUCCEEDED":
        # Extract detected text
        documentText = ""
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                documentText += item["Text"] + " "

        # Remove quotation marks
        documentText = documentText.replace(chr(34), '')
        documentText = documentText.replace(chr(39), '')

        # Delete the file from S3
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"Deleted s3://{bucket_name}/{object_name}")

        return documentText
    else:
        raise Exception("Document analysis failed.")






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



    def analyze(self):
        client = OpenAI(api_key=self.key)
        text =analyze_text_from_pdf_s3(self.pdf)
        # text+=im_text
        if len(text)==0:
            return ""
        else:
            message = [
                {"role": "system", "content": "You are a medical report analyzer."},
                {"role": "user", "content": f" Analyze the following medical reports extracted from the PDF and information extracted from images. Merge the information and provide a detailed, structured analysis without adding a summary: {text}"}

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
        {"role": "system", "content": "You are a quetion answer bot."},
        {"role": "user", "content": f"Analyze the following information and answer the query and answer the query only given from the given infomation and should know the basic meaning of medical term in the report: {info}\n\nUser Query: {query}"}
    ]
  
        response = client.chat.completions.create(
            model="gpt-4o", 
            messages=message
        )
        return response.choices[0].message.content

        


        


