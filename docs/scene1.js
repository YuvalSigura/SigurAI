import * as THREE from 'three';
import { FontLoader } from 'three/addons/FontLoader.js';
import { TextGeometry } from 'three/addons/TextGeometry.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, innerWidth/innerHeight, 0.1, 100);
camera.position.set(0, 0, 10);

const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('canvas'), antialias: true });
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(devicePixelRatio);

// Office screen placeholder
const screenGeo = new THREE.PlaneGeometry(4, 2.5);
const screenMat = new THREE.MeshBasicMaterial({ color: 0x333355 });
const screen = new THREE.Mesh(screenGeo, screenMat);
screen.position.set(0, -1, 0);
scene.add(screen);

// Ambient dimming light
const ambient = new THREE.AmbientLight(0xffffff, 1);
scene.add(ambient);

// Load font and generate text bubbles
new FontLoader().load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', font => {
  const bubbleTexts = [
    "Scan the network", "Check for vulnerabilities",
    "Update configurations", "Analyze logs"
  ];
  
  const bubbles = bubbleTexts.map((text, i) => {
    const geom = new TextGeometry(text, {
      font, size: 0.3, height: 0.02
    });
    const mat = new THREE.MeshBasicMaterial({ color: 0xffffff });
    const mesh = new THREE.Mesh(geom, mat);
    mesh.position.set((Math.random()-0.5)*6, -3 - i, 0);
    scene.add(mesh);
    return mesh;
  });

  // Animate
  let start = performance.now();
  function animate() {
    const t = (performance.now() - start) / 1000;
    ambient.intensity = Math.max(0.3, 1 - t * 0.1);

    bubbles.forEach((b, idx) => {
      b.position.y += 0.01 + idx * 0.005;
      if (b.position.y > 5) b.position.y = -4 - Math.random() * 2;
    });

    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }
  animate();
});

// Responsive
window.addEventListener('resize', () => {
  camera.aspect = innerWidth/innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
