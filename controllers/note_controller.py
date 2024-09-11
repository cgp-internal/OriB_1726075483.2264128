from flask import request, jsonify
from models.Note import Note

def create_note():
    new_note = Note(user=request.json['user'], note1=request.json['note1'], note2=request.json['note2'], 
                    image1=request.json['image1'], image2=request.json['image2'], image3=request.json['image3'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify({'message': 'Note created successfully'}), 201

def get_note(note_id):
    note = Note.query.get(note_id)
    if note is None:
        return jsonify({'message': 'Note not found'}), 404
    return jsonify({'id': note.id, 'user': note.user, 'note1': note.note1, 'note2': note.note2, 
                    'image1': note.image1, 'image2': note.image2, 'image3': note.image3}), 200

def update_note(note_id):
    note = Note.query.get(note_id)
    if note is None:
        return jsonify({'message': 'Note not found'}), 404
    if 'user' in request.json:
        note.user = request.json['user']
    if 'note1' in request.json:
        note.note1 = request.json['note1']
    if 'note2' in request.json:
        note.note2 = request.json['note2']
    if 'image1' in request.json:
        note.image1 = request.json['image1']
    if 'image2' in request.json:
        note.image2 = request.json['image2']
    if 'image3' in request.json:
        note.image3 = request.json['image3']
    db.session.commit()
    return jsonify({'message': 'Note updated successfully'}), 200

def delete_note(note_id):
    note = Note.query.get(note_id)
    if note is None:
        return jsonify({'message': 'Note not found'}), 404
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note deleted successfully'}), 200