// interactivity.js – Optional enhancements for SigurAI stealth page

document.addEventListener("DOMContentLoaded", () => {
  const footer = document.querySelector("footer");

  // Smooth fade-in effect for the main content after header loads
  const mainContent = document.querySelector("main");
  if (mainContent) {
    mainContent.style.opacity = 0;
    setTimeout(() => {
      mainContent.style.transition = "opacity 1.5s ease-in-out";
      mainContent.style.opacity = 1;
    }, 200); // Small delay after header for smoother transition
  }

  // Example: Subtle animation effect on footer when page is fully loaded
  if (footer) {
    footer.style.opacity = 0;
    setTimeout(() => {
      footer.style.transition = "opacity 1.5s ease-in-out";
      footer.style.opacity = 1;
    }, 500);
  }

  // Dynamic year update for copyright
  const year = new Date().getFullYear();
  const copyright = document.querySelector("footer");
  if (copyright) {
    copyright.innerHTML = `&copy; ${year} SigurAI. All rights reserved.`;
  }
});
