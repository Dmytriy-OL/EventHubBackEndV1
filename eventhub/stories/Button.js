import './button.css';

export default function Button({ label, size, primary }) {
  const mode = primary ? 'primary' : 'secondary';
  return `<button class="btn ${mode} ${size}">${label}</button>`;
}
