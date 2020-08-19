async function chooseFile() {

    let content = await eel.getFile()();
    document.getElementById('content').innerHTML = content;
}
async function saveFile() {

    let content = await eel.saveFile()();
    document.getElementById('filePath').innerHTML = `file path ${content}`;
}