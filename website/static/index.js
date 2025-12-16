function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ noteId: noteId }),
    }).then((res) => res.json())
        .then((data) => {
            if (data.success) {
                // Redirect with success parameter
                window.location.href = "/?deleted=true";
            } else {
                // Redirect without parameter on failure
                window.location.href = "/";
            }
        });
}