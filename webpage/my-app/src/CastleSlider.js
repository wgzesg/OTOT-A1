import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import MuiInput from '@mui/material/Input';

const Input = styled(MuiInput)`
  width: 42px;
`;

export default function CastleSlider({idx, onChange, value}) {
  const handleSliderChange = (event, newValue) => {
    onChange(idx, newValue);
  };

  const handleInputChange = (event) => {
    onChange(idx, event.target.value === '' ? 0 : Number(event.target.value));
  };

  const handleBlur = () => {
    if (value < 0) {
      onChange(idx, 0);
    } else if (value > 100) {
      onChange(idx, 100);
    }
  };

  return (
    <Box sx={{ height: 250 }}>
      <Grid item xs>
      <Typography id="input-slider" gutterBottom>
        Castle {idx+1}
      </Typography>
        </Grid>
      <Grid item xs height={200}>
        <Slider orientation="vertical"
          value={typeof value === 'number' ? value : 0}
          onChange={handleSliderChange}
          aria-labelledby="input-slider"
        />
      </Grid>
      <Grid item>
        <Input
          value={value}
          size="small"
          onChange={handleInputChange}
          onBlur={handleBlur}
          color="primary"
          inputProps={{
            step: 5,
            min: 0,
            max: 100,
            type: 'number',
            'aria-labelledby': 'input-slider',
            color: 'secondary'
          }}
        />
      </Grid>
    </Box>
  );
}