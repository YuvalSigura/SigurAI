// interactivity.js – Optional enhancements for SigurAI stealth page

document.addEventListener("DOMContentLoaded", () => {
  const footer = document.querySelector("footer");

  // Example: Subtle animation effect on footer when page is fully loaded
  if (footer) {
    footer.style.opacity = 0;
    setTimeout(() => {
      footer.style.transition = "opacity 1.5s ease-in-out";
      footer.style.opacity = 1;
    }, 500);
  }

  // Example: Dynamic year update (optional if not hardcoded)
  const year = new Date().getFullYear();
  const copyright = document.querySelector("footer");
  if (copyright) {
    copyright.innerHTML = `&copy; ${year} SigurAI. All rights reserved.`;
  }
});
