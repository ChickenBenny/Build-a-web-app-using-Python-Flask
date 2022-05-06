function deleteNote(noteId){
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

function deleteQuestion(questionId){
    fetch("/delete-question", {
        method: "POST",
        body: JSON.stringify({ questionId: questionId}),
    }).then((_res) => {
        window.location.href = "/meeting";
    })
}