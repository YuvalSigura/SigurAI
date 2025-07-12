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
import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById('three-bg'),
  alpha: true
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);

// Light
const ambient = new THREE.AmbientLight(0xffffff, 0.8);
scene.add(ambient);

// Texture loader
const loader = new THREE.TextureLoader();
const texture = loader.load('../images/icon.png'); // your phoenix

// Plane geometry with texture
const geometry = new THREE.PlaneGeometry(3, 3);
const material = new THREE.MeshBasicMaterial({ map: texture, transparent: true });
const logoMesh = new THREE.Mesh(geometry, material);
scene.add(logoMesh);

// Animate rotation
function animate() {
  requestAnimationFrame(animate);
  logoMesh.rotation.z += 0.002;
  renderer.render(scene, camera);
}
animate();

// Handle window resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth/window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
