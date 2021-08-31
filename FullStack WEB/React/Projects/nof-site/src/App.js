import { Route, Switch } from 'react-router-dom';

import CalculatorPage from './pages/CalculatorPage';
//import NewMeetupPage from './pages/NewMeetup';
//import FavoritesPage from './pages/Favorites';
import Layout from './components/layout/Layout';

function App() {
  return (
    <Layout>
      <Switch>
        <Route path='/' exact>
          <CalculatorPage />
        </Route>

        <Route path='/Calculator'>
          <CalculatorPage />
        </Route>
        
        <Route path='/favorites'>
        </Route>
      </Switch>
    </Layout>
  );
}

export default App;