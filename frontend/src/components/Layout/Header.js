import {
  AppBar,
  Button,
  IconButton,
  Toolbar,
  Typography,
} from '@material-ui/core';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import MenuIcon from '@material-ui/icons/Menu';
import Axios from 'axios';
import React from 'react';
import { Link, Redirect } from 'react-router-dom';
import AuthContext from '../../AuthContext';
import { drawerWidth, url } from '../../utils/constants';
import PollToggle from '../PollToggle';

const useStyles = makeStyles((theme) => ({
  appBar: {
    marginLeft: drawerWidth,
    [theme.breakpoints.up('sm')]: {
      width: `calc(100% - ${drawerWidth}px)`,
    },
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
  logoutButton: {
    float: 'right',
  },
}));

function Header({ handleMenuToggle = () => {} }) {
  const classes = useStyles();
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up('sm'));
  const token = React.useContext(AuthContext);
  const [loggedOut, setLoggedOut] = React.useState(false);

  if (loggedOut) {
    Axios.post(`${url}/auth/logout`, { token })
      .then((response) => {
        console.log(response);
      })
      .catch((err) => {
        console.error(err);
        // toast.error(DEFAULT_ERROR_TEXT);
      });
    localStorage.removeItem('token');
    return <Redirect to="/login" />;
  }

  return (
    <AppBar position="fixed" className={classes.appBar}>
      <Toolbar>
        {!matches && (
          <>
            <IconButton
              color="inherit"
              aria-label="open drawer"
              edge="start"
              onClick={handleMenuToggle}
              className={classes.menuButton}
            >
              <MenuIcon />
            </IconButton>
            <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>
              <Typography variant="h5" noWrap>
                Slackr
              </Typography>
            </Link>
          </>
        )}
        <div variant="h6" className={classes.title}>

        </div>
        <div style={{display:'flex'}}>
          <PollToggle />
          <Button
            color="inherit"
            className={classes.logoutButton}
            onClick={() => {
              setLoggedOut(true);
            }}
          >
            Logout
          </Button>
        </div>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
