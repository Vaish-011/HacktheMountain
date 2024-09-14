from flask import Flask, request, jsonify
from chemNEETData import chem_NEET_data
from phyNEETData import phy_NEET_data
from bioNEET import bio_data
from phyData import phy_data
from chemData import chem_data
from methsData import MathsData
from flask_cors import CORS
from highLight import highLight
from basetoimage import main
import base64 
app = Flask(__name__)

import pandas as pd
CORS(app=app)
@app.route('/get-example', methods=['GET'])
def get_example():
    data = {
        'message': 'This is a GET request',
        'status': 'success'
    }
    return jsonify(data)
  
  


@app.route('/Jee_Maths', methods=['POST'])
def methsData():
    try:
        # Retrieve the paragraph, files, and formOfDocument
        data = request.get_json()
        paragraph = data.get('paragraph', '')
        formOfDocument = int(data.get('formOfDocument', 0))
        quetionsFile = 'csvFiles/Final_Maths_Jee.csv'
        TotalMathsMergedData = 'csvFiles/TotalMathsMergedData.csv'

        # Call MathsData function with the inputs
        result = MathsData(paragraph=paragraph, TotalMathsMergedData=TotalMathsMergedData, quetionsFile=quetionsFile, formOfDocument=formOfDocument)

        # If MathsData returns a result, include it in the response
        return jsonify({"message": "Data processed successfully!", "result": result}), 200

    except Exception as e:
        # Catch and log any errors that occur
        print("Error in processing:", e)
        return jsonify({"error": "Failed to process data"}), 500
@app.route('/Jee_Chemistry',methods=['POST'])
def chemData():
    file = "D:\\hackethon_2\\csvFiles\\Jc.csv"
    posted_data = request.get_json()

    paragraph = posted_data['text']
    
    
    return chem_data(file , paragraph)

@app.route('/Jee_Physics',methods=['POST'])
def phyData():
    file = "D:\\hackethon_2\\csvFiles\\Jp.csv"
    posted_data = request.get_json()

    paragraph = posted_data['text']
    
    return phy_data(file,paragraph)

@app.route('/NEET_bio',methods=['POST'])
def bioData():


    file = "D:\\hackethon_2\\csvFiles\\Nb.csv"

    
    posted_data = request.get_json()

    paragraph = posted_data['text']
    
    
    return bio_data(file,paragraph)

@app.route('/NEET_chem',methods=['POST'])
def chemNEETData():


    
    file = "D:\\hackethon_2\\csvFiles\\Nc.csv"

    
    posted_data = request.get_json()

    paragraph = posted_data['text']
    
    
    return chem_NEET_data(file,paragraph)

@app.route('/NEET_phy',methods=['POST'])
def phyNEETData():

   
    file = "D:\\hackethon_2\\csvFiles\\Np.csv"

    posted_data = request.get_json()

    paragraph = posted_data['text']
        
    
    
    return phy_NEET_data(file,paragraph)

@app.route('/GetHighLight', methods=['POST'])
def HighLight():
    if 'file' not in request.files or 'pageNumber' not in request.form:
        return jsonify({'error': 'File or page number missing'}), 400

    file = request.files['file']
    page_number = int(request.form['pageNumber'])
    return highLight(file=file , page_number=page_number)

@app.route('/Text_extract', methods=['POST'])
def extracted_text():
    file = request.get_json()
    subject = file.get("Subject")
    base_string = file.get('ImageBase64String')

    # Add padding to the Base64 string if needed
    base_string += '=' * (-len(base_string) % 4)
    # print(base_string)
    try:
        result = main(base_string)
        # print(type(result))
        if subject=="Jc":
            filePath = "D:\\hackethon_2\\csvFiles\\Jc.csv"
            return chem_data(filePath,result)
        elif subject=="Jp":
            filePath = "D:\\hackethon_2\\csvFiles\\Jp.csv"
            return phy_data(filePath,str(result))
        elif subject=="Nb":
            filePath = "D:\\hackethon_2\\csvFiles\\Nb.csv"
            return bio_data(filePath,str(result))
        elif subject=="Nb":
            filePath = "D:\\hackethon_2\\csvFiles\\Nc.csv"
            return chem_NEET_data(filePath,str(result))
        elif subject=="Nb":
            filePath = "D:\\hackethon_2\\csvFiles\\Np.csv"
            return phy_NEET_data(filePath,str(result))
        elif subject=="Nb":
            filePath = "D:\\hackethon_2\\csvFiles\\Jm.csv"
            return MathsData(filePath,str(result))
        else:
            return jsonify({"Sorry yarr kuch nhi h!!"}, 404) 
       
    
    except Exception as e:
        # Log and return any errors that occur
        print("Error in text extraction:", e)
        return jsonify({"error": "Failed to extract text"}), 500
if __name__ == '__main__':
    app.run(debug=True)
