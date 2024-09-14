from flask import Flask, request, jsonify
from methsData import MathsData
from flask_cors import CORS
app = Flask(__name__)

@app.route("/Jee_Maths" , methods=['POST'])
def mathsData():
    try:
        # Retrieve the paragraph, files, and formOfDocument
        data = request.get_json()
        paragraph = data.get('paragraph', '')
        formOfDocument = int(data.get('formOfDocument', 0))
        quetionsFile = r'csvFiles/Final_Maths_Jee.csv'
        TotalMathsMergedData = r'csvFiles/TotalMathsMergedData.csv'

        
        result = MathsData(paragraph=paragraph, TotalMathsMergedData=TotalMathsMergedData, quetionsFile=quetionsFile, formOfDocument=formOfDocument)

       
        return jsonify({"message": "Data processed successfully!", "result": result}), 200

    except Exception as e:
       
        print("Error in processing:", e)
        return jsonify({"error": "Failed to process data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
