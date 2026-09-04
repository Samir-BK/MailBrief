document.getElementById("askform").onsubmit = async (e) => {
  e.preventDefault();
  let formData = new FormData(e.target);

  let loading = document.getElementById("ask-loading");
  loading.style.display = "block"; // show loader

  let res = await fetch("/ask", {
    method: "POST",
    body: formData,
  });

  let data = await res.json();
  document.getElementById("answer").innerText = data.response;

  loading.style.display = "none"; // hide loader
};
