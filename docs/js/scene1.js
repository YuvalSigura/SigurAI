import * as THREE from 'three';
import { FontLoader } from 'three/addons/loaders/FontLoader.js';
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, innerWidth / innerHeight, 0.1, 100);
camera.position.z = 10;

const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('canvas'), antialias: true });
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(devicePixelRatio);

// Background light setup
const ambientLight = new THREE.AmbientLight(0xffffff, 1);
scene.add(ambientLight);

// Screen (placeholder for person)
const screen = new THREE.Mesh(
  new THREE.PlaneGeometry(4, 2.5),
  new THREE.MeshBasicMaterial({ color: 0x333355 })
);
screen.position.set(0, -2, 0);
scene.add(screen);

// Bubble data
const tasks = [
  "Scan the network",
  "Check for vulnerabilities",
  "Update configurations",
  "Analyze logs",
  "Fix SSL issues",
  "Review firewall",
  "Dump credentials",
  "Generate report"
];

const loader = new FontLoader();
loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', font => {
  const bubbleGroup = new THREE.Group();

  tasks.forEach((task, i) => {
    const textGeo = new TextGeometry(task, {
      font: font,
      size: 0.3,
      height: 0.02,
    });
    textGeo.center();

    const textMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
    const textMesh = new THREE.Mesh(textGeo, textMat);

    const bubble = new THREE.Mesh(
      new THREE.PlaneGeometry(task.length * 0.2, 0.6),
      new THREE.MeshBasicMaterial({ color: 0x2a2a2a, transparent: true, opacity: 0.6 })
    );

    const wrapper = new THREE.Group();
    wrapper.add(bubble);
    wrapper.add(textMesh);
    textMesh.position.z = 0.01;

    wrapper.position.set((Math.random() - 0.5) * 6, -3 - i * 1.2, 0);
    bubbleGroup.add(wrapper);
  });

  scene.add(bubbleGroup);

  // Animation
  const start = performance.now();
  function animate() {
    const t = (performance.now() - start) / 1000;
    ambientLight.intensity = Math.max(0.2, 1 - t * 0.1);

    bubbleGroup.children.forEach((b, idx) => {
      b.position.y += 0.01 + idx * 0.001;
      if (b.position.y > 5) b.position.y = -4 - Math.random() * 2;
    });

    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }

  animate();
});

window.addEventListener('resize', () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
