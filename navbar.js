// Importing necessary React hooks and components
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/img/favicon.png';
import light from '../assets/svg/light.svg';
import dark from '../assets/svg/dark.svg';

/**
 * Functional component representing the navigation bar.
 */
function Navbar() {
  // State to manage the theme (light/dark)
  const [theme, setTheme] = useState(false);

  // Function to handle theme toggle
  const handleClick = () => {
    setTheme(!theme);

    // Saving the selected theme to localStorage
    localStorage.setItem('theme', theme ? 'dark' : 'light');
  }

  // useEffect to handle theme initialization and updates
  useEffect(() => {
    // Applying the selected theme from localStorage
    if (localStorage.getItem('theme') === 'light') {
      document.body.classList.remove('dark');
    } else if (localStorage.getItem('theme') === 'dark') {
      document.body.classList.add('dark');
    } else {
      document.body.classList.remove('dark');
    }
  }, [theme]);

  // JSX structure for the navigation bar
  return (
    <nav>
      {/* Top navigation bar start */}
      <div className='top-nav'>
        <div className='left'>
          <img src={logo} alt='LSPU-logo' />
          <span>E-Sentry | Laguna State Polytechnic University - Los Baños Campus</span>
        </div>
        <div className='right'>
          <ul>
            <li>
              <Link to="/accessibility">
                Accessibility
              </Link>
            </li>
            <li>
              <Link to="/contact-us">
                Contact Us
              </Link>
            </li>
            <li>
              <input type='search' placeholder='Search items here...' />
            </li>
          </ul>
        </div>
      </div>
      {/* Top navigation bar end */}

      {/* Navigation bar start */}
      <div className='navbar'>
        <div className='left'>
          <img src={logo} alt='logo' />
        </div>
        <div className='right'>
          <ul>
            <li>
              <Link to='/'>
                Home
              </Link>
            </li>
            <li>
              <Link to='/about-sentry'>
                About E-Sentry
              </Link>
            </li>
            <li>
              <Link to='/about-us'>
                About Us
              </Link>
            </li>
            <li>
              <img src={theme ? light : dark} className="toggle-ic" onClick={handleClick} alt={`Toggle ${theme ? 'light' : 'dark'} theme`} />
            </li>
          </ul>
        </div>
      </div>
      {/* Navigation bar end */}
    </nav>
  );
}

// Exporting the Navbar component as the default export
export default Navbar;
