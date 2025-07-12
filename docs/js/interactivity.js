// interactivity.js – Optional enhancements for SigurAI stealth page

document.addEventListener("DOMContentLoaded", () => {
  const footer = document.querySelector("footer");
  const mainContent = document.querySelector("main");

  // Smooth fade-in effect for the main content after header loads
  if (mainContent) {
    mainContent.style.opacity = 0;
    setTimeout(() => {
      mainContent.style.transition = "opacity 1.5s ease-in-out";
      mainContent.style.opacity = 1;
    }, 200);
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

  // --- New "Cool" JavaScript Effects ---

  // Scroll-triggered fade-in for feature items
  const featureItems = document.querySelectorAll('.feature-item');
  const observerOptions = {
    root: null, // relative to the viewport
    rootMargin: '0px',
    threshold: 0.2 // Trigger when 20% of the item is visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
        observer.unobserve(entry.target); // Stop observing once animated
      }
    });
  }, observerOptions);

  featureItems.forEach(item => {
    observer.observe(item);
  });
});
