import React from 'react';
import { Typography, Button, Divider, Stack, Card, Grid } from '@mui/material';
import CastleSlider from './CastleSlider';

class GamePage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {remain: 100};
    this.num_castle = 10;
    for (let i = 0; i < this.num_castle; i++) {
      this.state[i] = 0;
    }
  }

  handleSliderChange = (castle_id, value) => {
    const old_val = this.state[castle_id];
    const change = value - old_val;
    if (change > this.state['remain']) {
      return;
    }
    let res = this.state['remain'] - value + this.state[castle_id];
    this.setState({ remain: res });
    console.log("value of remain is " + this.state['remain'])
    this.setState({ [castle_id]: value });
    console.log("value of castle " + castle_id + " is " + value)
  };

  render() {
    const items = [];
    for (let i = 0; i < this.num_castle; i++) {
      items.push(<CastleSlider key={i} idx={i} onChange={this.handleSliderChange} value={this.state[i]}/>);
    }
    return (
      <div className="App Game">
      <div>
        <h1>
          Game
        </h1>
      </div>
      <Grid container spacing={5}>
        <Grid item xs={3} spacing={5}>
          <Card>  items</Card>
          <Card>  items</Card>
          <Card>  items</Card>
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
              <Button variant="contained" size='small' className='Button'>Submit</Button>
            </div>
          </Stack>
        </Grid>
      </Grid>
    </div>
    )
  }
}

export default GamePage;