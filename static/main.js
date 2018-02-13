// async function postText(evt) {
//   evt.preventDefault()
  
//   const text = evt.target['input'].value
//   const blah = JSON.stringify(text)
//   console.log(blah)
//   const res = await fetch('/predict', {
//       blah,
//       method: "POST",
//       headers: {
//           'content-type': 'application/json',
//           'accept': 'application/json',
//       }})
//   const json = await res.json()
//   console.log(json)
// }

// document.forms.thai.addEventListener('submit', postText)