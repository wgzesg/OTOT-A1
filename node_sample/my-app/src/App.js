import './App.css';
import Button from '@mui/material/Button';

function App() {
  return (
    <div className="App App-header">
      <div>
        <h1>
          Welcome to the Battle for Riddler Nation
        </h1>
      </div>
      <div className="App">
        <Button variant="contained" size='big' className='Button' href="/game"> Start Game </Button>
        <br></br> <br></br>
        <Button variant="contained" size='big' className='Button' href="/rules"> Rules  </Button>
      </div>
    </div>
  );
}

export default App;
