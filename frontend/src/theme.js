import { red } from '@material-ui/core/colors';
import { createMuiTheme } from '@material-ui/core/styles';

// A custom theme for this app
const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#0A0A0A',
    },
    secondary: {
      main: '#ff3399',
    },
    error: {
      main: red.A400,
    },
    background: {
      default: '#D3D3D3',
    },
  },
});

export default theme;
