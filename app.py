from flask import Flask, request, jsonify
from models.Note import Note

app = Flask(__name__)

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    note = Note(user=data['user'], note1=data['note1'], note2=data['note2'], image1=data['image1'], image2=data['image2'], image3=data['image3'])
    db.session.add(note)
    db.session.commit()
    return jsonify({'message': 'Note created successfully'}), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    output = []
    for note in notes:
        note_data = {}
        note_data['id'] = note.id
        note_data['user'] = note.user
        note_data['note1'] = note.note1
        note_data['note2'] = note.note2
        note_data['image1'] = note.image1
        note_data['image2'] = note.image2
        note_data['image3'] = note.image3
        output.append(note_data)
    return jsonify({'notes': output})

@app.route('/notes/<note_id>', methods=['GET'])
def get_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note is None:
        return jsonify({'message': 'Note not found'}), 404
    note_data = {}
    note_data['id'] = note.id
    note_data['user'] = note.user
    note_data['note1'] = note.note1
    note_data['note2'] = note.note2
    note_data['image1'] = note.image1
    note_data['image2'] = note.image2
    note_data['image3'] = note.image3
    return jsonify({'note': note_data})

@app.route('/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note is None:
        return jsonify({'message': 'Note not found'}), 404
    data = request.get_json()
    note.user = data['user']
    note.note1 = data['note1']
    note.note2 = data['note2']
    note.image1 = data['image1']
    note.image2 = data['image2']
    note.image3 = data['image3']
    db.session.commit()
    return jsonify({'message': 'Note updated successfully'})

@app.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note is None:
        return jsonify({'message': 'Note not found'}), 404
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)