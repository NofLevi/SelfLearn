import { useContext } from 'react';
import { Link } from 'react-router-dom';

import classes from './MainNavigation.module.css';

function MainNavigation() {
  return (
    <header className={classes.header}>
      <div className={classes.logo}>Nof Narcisistic Site</div>
      <nav>
        <ul>
          <li>
            <Link to='/Calculator'>Calculator</Link>
          </li>
          <li>
            <Link to='/Map'>Map</Link>
          </li>
          <li>
            <Link to='/temp2'>
              temp2
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;
