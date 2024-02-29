window.addEventListener('DOMContentLoaded', () => {
    if (window.location.href.includes('addtest')) {
        const button = document.querySelector('button.add-question')

        const addQuestionInput = () => {
            const nextPElement = document.createElement('p')
            nextPElement.innerHTML = `<input type="text" name="question" maxlength="255" required="" id="id_question" />`
            const inputs = document.querySelectorAll('input[type="text"]')
            const last = inputs.length - 1
            inputs[last].parentElement.after(nextPElement)
        }

        button.addEventListener('click', () => {
            addQuestionInput()
        })
    }
})