const gridContainer = document.querySelector('.grid-container')

function displayResponse(text) {
  let div = document.querySelector('.tokenized')

  if (!div) {
    div = document.createElement('div')
    div.classList.add('tokenized')
    gridContainer.appendChild(div)
  }
  div.innerText = text
}

async function handleSubmit(evt) {
  evt.preventDefault()
  const textArea = evt.target['text']
  const body = JSON.stringify({ text: textArea.value })

  const response = await fetch('/predict', {
    body,
    method: 'POST',
    headers: {
      'content-type': 'application/json'
    },
  })
  const json = await response.json()

  if ('tokenized' in json) {
    displayResponse(json.tokenized)
  }

  textArea.focus()
}

document
  .forms['thai-form']
  .addEventListener('submit', handleSubmit)