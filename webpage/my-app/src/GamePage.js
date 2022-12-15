import React from 'react';
import { Typography, Button, Divider, Stack, Grid, Box } from '@mui/material';
import { blueGrey } from '@mui/material/colors';
import CastleSlider from './CastleSlider';
import axios from 'axios';
import ResultCard from './ResultCard';
import { config } from './Constant';

class GamePage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {remain: 100};
    this.num_castle = 10;
    this.state.castle = Array(10).fill(0);
    console.log(this.state.castle)
    this.state.past = {games: []};
    this.ref = React.createRef()
  }

  handleSliderChange = (castle_id, value) => {
    const old_val = this.state.castle[castle_id];
    const change = value - old_val;
    if (change > this.state['remain']) {
      return;
    }
    let res = this.state['remain'] - value + this.state.castle[castle_id];
    this.setState({ remain: res });
    console.log("value of remain is " + this.state['remain'])
    let copy = this.state.castle.slice();
    copy[castle_id] = value;
    this.setState({ castle: copy });
    console.log("value of castle " + castle_id + " is " + value)
  };

  handleClick = () => {
    console.log("clicked");
    const past = this.state.past;
    axios.post(config.url.API_URL + '/infer', { past })
    .then(res => {
      console.log("received response");
      const ai_action = res.data['data'];
      console.log(ai_action);
      const human_action = this.state.castle;
      this.setState({ past: { games: [...past.games, { human: human_action, ai: ai_action }] } });
    })
  }

  componentDidMount () {
    this.ref.current?.scrollIntoView({behavior: 'smooth'});
  }

  componentDidUpdate () {
    this.ref.current?.scrollIntoView({behavior: 'smooth'});
  }

  render() {
    const items = [];
    for (let i = 0; i < this.num_castle; i++) {
      items.push(<CastleSlider key={i} idx={i} onChange={this.handleSliderChange} value={this.state.castle[i]}/>);
    }
    const result = this.state.past.games.map((game, idx) => {
      return (
        <ResultCard key={idx} idx={idx} ai={game.ai} human={game.human}/>
      )
    });

    return (
      <div className="App Game">
      <div>
        <h1>
          Battle of Riddler Nation
        </h1>
      </div>
      <Grid container spacing={5} paddingLeft={10} paddingBottom={5}>
        <Grid item xs={3} spacing={5} padding={5}>
        <Box width={1} height={400} sx={{ alignItems: 'center', p: 1, border: 1, bgcolor: blueGrey[200], borderRadius: 2, scrollBehavior: 'smooth', overflowY: 'scroll' }}>
          <Stack spacing={1} >
           {result}
           <div ref={this.ref}></div>
          </Stack>
        </Box>
        </Grid>
        <Grid item xs={8}>
          <Stack spacing={8}>
            <div>
              <Typography>Number of Soldiers remaining: {this.state.remain  }</Typography>
            </div>

            <Stack direction="row" spacing={2} divider={<Divider orientation="vertical" />}>
              {items}
            </Stack>
            <div>
              <Button variant="contained" size='small' className='Button' onClick={this.handleClick} >Submit</Button>
            </div>
          </Stack>
        </Grid>
      </Grid>
    </div>
    )
  }
}

export default GamePage;