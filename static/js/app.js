//  const sign_in_btn = document.querySelector("#sign-in-btn");
 //const sign_up_btn = document.querySelector("#sign-up-btn");
const submit_in = document.querySelector("#btn-solid");
const submit_out = document.querySelector("#singup");
//const sign_up_btn = document.querySelector("#btn solid");
const container = document.querySelector(".container");

submit_in.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});
submit_out.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

// sign_in_btn.addEventListener("click", () => {
//   container.classList.remove("sign-up-mode");
// });