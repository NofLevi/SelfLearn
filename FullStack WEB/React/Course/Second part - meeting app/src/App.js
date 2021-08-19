import { Route , Switch} from 'react-router-dom'

import MainNavigation from './components/layout/MainNavigation';
import AllMeetupsPage from './pages/AllMeetups';
import NewMeetupPage from './pages/NewMeetup';
import FavoritesPage from './pages/Favorites';

function App() {
  // localhost:3000/path
  // my-page.com/path
  return (
    <div>
      <MainNavigation/>
      <Switch>
        <Route path = '/' exact = {true}> 
          <AllMeetupsPage />
        </Route>

        <Route path = '/new-meetup'>
            <NewMeetupPage/>
        </Route>

        <Route path = '/favorites'>
            <FavoritesPage/>
        </Route>
      </Switch>

    </div>
  );
}

export default App;