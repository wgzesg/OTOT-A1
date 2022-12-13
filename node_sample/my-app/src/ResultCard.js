import { Typography, Card, CardContent, Chip, Stack, Tooltip } from '@mui/material';
import { teal, red, green, grey } from '@mui/material/colors';
import React from 'react';

export default class ResultCard extends React.Component {

  constructor(props) {
    super(props);
    this.human = props.human;
    this.ai = props.ai;
    this.idx = props.idx;
  }

  render() {
    const dots = this.ai.map((ai_num, index) => {
      console.log("ai", + ai_num, this.human[index])
      const color = ai_num < this.human[index] ? teal[700] : ai_num > this.human[index] ? red[700] : 'grey';
      return (
        <Tooltip title={"You " + this.human[index] + " : " + ai_num +" Computer"}>
          <Chip
            key={index}
            sx={{ bgcolor: color, width: 15, height: 15 }}
            onClick={() => {}}
          />
        </Tooltip>
      );
    });

    let human_score = 0;
    let ai_score = 0;
    for (let i = 0; i < this.human.length; i++) {
      if (this.human[i] > this.ai[i]) {
        human_score += i+1;
      } else if (this.human[i] < this.ai[i]) {
        ai_score += i+1;
      } else {
        human_score += (i+1) / 2;
        ai_score += (i+1) / 2;
      }
    }
    const bg_color = human_score > ai_score ? green[300] : human_score < ai_score ? red[200] : grey[300];
    return (

      <Card>

        <CardContent sx={{ bgcolor: bg_color }}>

          <Typography color='text.secondary' sx={{ fontSize:14}} gutterBottom>
            Game {this.props.idx + 1}: You {human_score} : {ai_score} Computer
          </Typography>
          <Stack direction='row' spacing={1} alignItems="center" justifyContent="center"> 
            {dots}
          </Stack>

        </CardContent>

      </Card>

    );

  }

}