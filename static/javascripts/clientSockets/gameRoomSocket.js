var lang = 'C';

socket.on("code-review-complete", (data) => {
    document.getElementById('text-result').value = data;
});

socket.on('lang-changed-returned', (code) => {
    console.log(code);
    //document.getElementById('text-code-ace').value = code;
    var text_code = document.getElementById('text-code');
    editor.setValue(code);
})


let review_code = () => {
    var text_code = document.getElementById('text-code');
    var code = editor.getValue();
    socket.emit("code-review", {code: code, lang: lang});
}

var c = document.getElementById('c');
var cpp = document.getElementById('cpp');
var py = document.getElementById('python');


c.classList.add('active1');
socket.emit('lang-changed', lang);


c.addEventListener('click', () => {
    c.classList.add('active1');
    cpp.classList.remove('active1');
    py.classList.remove('active1');
    lang = 'C';
    socket.emit('lang-changed', lang);
});

py.addEventListener('click', () => {
    py.classList.add('active1');
    cpp.classList.remove('active1');
    c.classList.remove('active1');
    lang = 'py';
    socket.emit('lang-changed', lang);
});

cpp.addEventListener('click', () => {
    cpp.classList.add('active1');
    py.classList.remove('active1');
    c.classList.remove('active1');
    lang = 'cpp';
    socket.emit('lang-changed', lang);
});