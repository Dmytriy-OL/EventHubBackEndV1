import { createButton } from './Button';
import './header.css';

export default function Header({ title, showLogo }) {
  return `<header>${showLogo ? '<img src="logo.png" alt="logo" />' : ''} ${title}</header>`;
}