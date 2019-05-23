# coding: utf-8

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, make_response, send_file
import StringIO
import pyexcel as pe
import csv

app = Flask(__name__)

currentId = 11
dinos = [{
    "id": 1,
    "name": "Triceratops",
    "meaning": "Three-horned face",
    "origin": "The name ‘Triceratops’ comes from the Greek language, with ‘tri’ meaning three and ‘keratops’ meaning horned face.",
    "details": "The Triceratops is one of the most easily recognizable dinosaurs due to its large body, unique frill and three horns."\
        "It is believed that fully grown Triceratops were about 8m (26ft) in length, 3m (10ft) in height and weighed anywhere between 6 to 12 tons.",
    "image": "http://www.sciencekids.co.nz/images/pictures/dinosaurs/triceratops/triceratopsillustration.jpg"
},
{
    "id": 2,
    "name": "Allosaurus",
    "meaning": "Different lizard",
    "origin": "The name is derived from the Greek words allos('different') and sauros('lizard').",
    "details": "Most Allosaurus fossils have been found in the Morrison Formation, a distinctive band of sedimentary rock found in the western United States."\
        "Allosaurus had a large skull and walked on two legs.",
    "image": "http://www.sciencekids.co.nz/images/pictures/dinosaurs/allosaurus.jpg"
},
{
    "id": 3,
    "name": "Spinosaurus",
    "meaning": "Spine lizard",
    "origin": "the dinosaur had very long spines growing on its back, measuring up to 7 feet (2.1 meters). ",
    "details": "The Spinosaurus lived around 100 million years ago in what is now North Africa. Fossils of the Spinosaurus were first found in Egypt around 1910."\
        "The Spinosaurus was larger than the Tyrannosaurus Rex and may have been the largest carnivorous (meat eating) dinosaur ever.",
    "image": "https://www.schleich-s.com/media/catalog/product/cache/17/small_image/600x/41ff4e9c985d00a9b9c6d7454ded3dd0/1/5/15009_main_v19_tp.jpg"
},
{
    "id": 4,
    "name": "Brachiosaurus",
    "meaning": "Arm lizard",
    "origin": "The Greek meaning of the name is arm-lizard because Brachiosaurus had longer forelimbs than hindlimbs.",
    "details": "The weight of Brachiosaurus has been estimated between 30 and 45 metric tons."\
         "The length of Brachiosaurus is believed to have been around 26 metres (85 feet)."\
              "It is estimated that Brachiosaurus ate between 200 and 400 kilograms (440 and 880 pounds) of plants every day!",
    "image": "http://www.sciencekids.co.nz/images/pictures/dinosaurs/brachiosaurusdrawing.jpg"
},
{
    "id": 5,
    "name": "Stegosaurus",
    "meaning": "Roof lizard",
    "origin": "The name ‘Stegosaurus’ comes from the Greek words ‘stegos’ meaning roof and ‘sauros’ meaning lizard.",
    "details": "The Stegosaurus is the most famous dinosaur from a group of dinosaurs known as Stegosauria. They were all herbivores (plant eaters) and featured rows of unique bones that developed into plates and spines along their back and tail. "\
            "The Stegosaurus was alive in the late Jurassic Period (around 150 million years ago).",
    "image": "http://www.sciencekids.co.nz/images/pictures/dinosaurs/stegosaurus/stegosaurusillustration.jpg"
},
{
    "id": 6,
    "name": "Ankylosaurus",
    "meaning": "Fused lizard",
    "origin": "Bones in its skull and other parts of its body were fused, making the dinosaur extremely rugged.",
    "details": "Ankylosaurus lived at the end of the Cretaceous Period (around 66 million years ago). The Ankylosaurus was a large dinosaur. The top of the dinosaur was almost completely covered with thick armor consisting of massive knobs and oval plates of bone, known as osteoderms or scutes, which are also common on crocodiles, armadillos and some lizards. "\
        "They were herbivores (plant eaters) and had small teeth relative to their body size.",
    "image": "https://previews.123rf.com/images/warpaintcobra/warpaintcobra1704/warpaintcobra170400020/85697703-ankylosaurus.jpg"
},
{
    "id": 7,
    "name": "Velociraptor",
    "meaning": "Swift seizer",
    "origin": "The name is derived from the Latin words velox(swift) and raptor(robber).",
    "details": "Velociraptor lived in the late Cretaceous Period (around 73 million years ago)."\
            "It played a large role in the Jurassic Park movies but was often shown inaccurately. Rather than being a larger, human sized dinosaur, the Velociraptor was around the size of a turkey.",
    "image": "http://images.dinosaurpictures.org/velociraptor_4d16.jpg"
},
{
    "id": 8,
    "name": "Tyrannosaurus",
    "meaning": "Tyrant lizard",
    "origin": "‘Tyrannosaurus’ comes from the Greek words meaning ‘tyrant lizard’, while the word ‘rex’ means ‘king’ in Latin.",
    "details": "Tyrannosaurus rex is often abbreviated to T-Rex."\
        "It walked on two legs, balancing its huge head with a long and heavy tail that sometimes contained over 40 vertebrae."\
            "Tyrannosaurus rex measured up to 13m (42ft) in length, 4m (13ft) at the hip and could weigh up to 7 tons!",
    "image": "http://nationaldinosaurmuseum.com.au/wp-content/uploads/2018/06/jurassic-world-fallen-kingdom.jpg"
},
{
    "id": 9,
    "name": "Carnotaurus",
    "meaning": "Meat eating bull",
    "origin": "Derived from Latin words carnis(flesh) and taurus(bull), the name is an allusion to the animal's carnivorous diet and bull-like horns.",
    "details": "Carnotaurus lived around 66 million years ago, before the mass extinction event that occurred at the end of the Cretaceous Period."\
        "Carnotaurus lived in an area of South America known as Patagonia. They were discovered in 1985 by a famous Argentine paleontologist named Jose Bonaparte.",
    "image": "https://previews.123rf.com/images/warpaintcobra/warpaintcobra1612/warpaintcobra161200032/70431034-carnotaurus.jpg"
},
{
    "id": 10,
    "name": "Diplodocus",
    "meaning": "Double beam",
    "origin": "The name is derived from the Greek words diplos(double) and dokos(beam)",
    "details": "The Diplodocus is a well known dinosaur that is popular in films, documentaries, as toy figurines and has been featured in a large number of museum exhibitions around the world."\
        "A large amount of fossil remains have made it easier for scientists to study the Diplodocus compared to many other dinosaurs."\
            "Research suggests the Diplodocus could have been as long as 35m (115ft) and around 10 to 15 tons in weight.",
    "image": "http://images.dinosaurpictures.org/diplodocus-michael-vigliotti_b410.jpg"
}
]

question_id = 3
questions = [{
    "id": 1,
    "text": "What does the name Carnotaurus stand for?",
    "options": ["Meat eating bull", "Tyrant lizard", "Swift seizer"],
    "image": "",
    "answer": "Meat eating bull"
},
{
    "id": 2,
    "text": "Did Triceratops have horns?",
    "options": ["True", "False"],
    "image": "",
    "answer": "True"
},
{
    "id": 3,
    "text": "What are the meanings of the words that make up T-Rex?",
    "options": ["Tryrant, Lizard, King", "Swift, Seizer, Bull", "Tyrant, Lizard, Meat"],
    "image": "https://cdna.artstation.com/p/assets/images/images/006/839/704/large/vitamin-imagination-1.jpg?1501637112",
    "answer": "Tryrant, Lizard, King"
},
{
    "id": 4,
    "text": "What does the name Velociraptor mean?",
    "options": ["Swift seizer", "Tyrant lizard", "Different lizard"],
    "image": "",
    "answer": "Swift seizer"
},
{
    "id": 5,
    "text": "What does sauros stand for in Greek?",
    "options": ["animal", "lizard", "reptile"],
    "image": "",
    "answer": "lizard"
},
{
    "id": 6,
    "text": "What does the name Diplodocus stand for?",
    "options": ["Double beam", "King", "Tyrant"],
    "image": "",
    "answer": "Double beam"
},
{
    "id": 7,
    "text": "Where does Spinosaurus get its name from?",
    "options": ["Large head", "Long spines", "Small hindlimbs"],
    "image": "",
    "answer": "Long spines"
},
{
    "id": 8,
    "text": "What does the name Brachiosaurus mean?",
    "options": ["Horned face", "Long lizard", "Arm lizard"],
    "image": "",
    "answer": "Arm lizard"
},
{
    "id": 9,
    "text": "What is the meaning of the words that make up Stegosaurus?",
    "options": ["Roof, lizard", "Spine, lizard", "Swift, seizer"],
    "image": "",
    "answer": "Roof, lizard"
},
{
    "id": 10,
    "text": "The name Allosaurus is derived from allos and sauros. What does allos stand for?",
    "options": ["Light", "Different", "Armour"],
    "image": "",
    "answer": "Different"
},
{
    "id": 11,
    "text": "What does the name Ankylosaurus stand for?",
    "options": ["Fat lizard", "Bull lizard", "Fused lizard"],
    "image": "",
    "answer": "Fused lizard"
}
]

@app.route('/home')
def home(name=None):
    return render_template('home.html', dinos=dinos)

@app.route('/viewdata')
def viewdata(name=None):
    return render_template('viewdata.html', dinos=dinos)

@app.route('/dinodata/<dino_id>')
def dinodata(dino_id=None):
    return render_template('dinodata.html', dinos=dinos, dino_id=dino_id)

@app.route('/trivia')
def trivia(name=None):
    return render_template('trivia.html', questions=questions, wrong_answers=wrong_answers)

@app.route('/getCSV', methods = ['GET'])
def getCSV():
    return send_file('DinoData.csv',
                     mimetype='text/csv',
                     attachment_filename="DinoData.csv",
                     as_attachment=True)

wrong_answers = {}

@app.route('/evaluate', methods = ['POST'])
def evaluate():
    
    # we would get a dictionary here, with question ids as keys and option index as values
    # based on the question index, use the questions array to evaluate if the answer is correct
    global wrong_answers
    wrong_answers = {}
    json_data = request.get_json()
    print(json_data)
    for key in json_data:
        # print(key)
        # firm = [k for k, v in questions if k==key]
        # print(firm)
        stripped_key = key.encode("ascii","replace")
        print(list(filter(lambda question: question['id'] == int(stripped_key), questions)))

        question_s = list(filter(lambda question: question['id'] == int(stripped_key), questions))
        if len(question_s) > 0:
            question = question_s[0]
            option_key = json_data[key].encode("ascii","replace")
            print(question['options'])
            print(int(option_key))
            answer = question['options'][int(option_key)-1]
            if answer != question['answer']:
                #wrong_answer_pair = {key: answer}
                wrong_answers[key] = answer
        

    return jsonify(questions=questions, wrong_answers=wrong_answers)


# def createCSV():
#     sheet = pe.Sheet(dinos)
#     io = StringIO.StringIO()
#     sheet.save_to_memory("csv", io)
#     output = make_response(io.getvalue())
#     output.headers["Content-Disposition"] = "attachment; filename=DinoData.csv"
#     output.headers["Content-type"] = "text/csv"
#     return output

def createCSV_file():
    csv_columns = ['id','name','period', 'found', 'description', 'details', 'image']
    csv_file = "DinoData.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dinos:
                writer.writerow(data)
    except IOError:
        print("I/O error") 

if __name__ == '__main__':
   app.config["CACHE_TYPE"] = "null"
   app.run(debug = True)
   #createCSV_file()