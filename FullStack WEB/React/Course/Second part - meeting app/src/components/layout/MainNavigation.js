import { Link } from 'react-router-dom'

import classes from './MainNavigation.module.css'

function MainNavigation(){
    return (
        <header className = {classes.header}>
            <div>React Meetups</div>
            <nav>
                <ul>
                    <li>
                        <Link to = '/'> SomeL</Link>
                    </li>
                    <li>
                        <Link to = '/'> SomeL</Link>
                    </li>
                    <li>
                        <Link to = '/'> SomeL</Link>
                    </li>
                </ul>
            </nav>
        </header>);
}


export default MainNavigation;