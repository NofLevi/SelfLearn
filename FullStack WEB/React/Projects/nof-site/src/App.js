import { Route, Switch } from 'react-router-dom';

import CalculatorPage from './pages/CalculatorPage';
import MapPage from './pages/MapPage';
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
        
        <Route path='/Map'>
          <MapPage/>
        </Route>
        
      </Switch>
    </Layout>
  );
}

export default App;