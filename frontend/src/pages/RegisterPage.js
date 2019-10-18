import {
  Avatar,
  Box,
  Button,
  Container,
  Grid,
  Link,
  makeStyles,
  TextField,
  Typography,
} from '@material-ui/core';
import DeveloperOutlinedIcon from '@material-ui/icons/DeveloperModeOutlined';
import Axios from 'axios';
import React from 'react';
import { url } from '../utils/constants';
import { toast } from 'react-toastify';
import { DEFAULT_ERROR_TEXT } from '../utils/text';

const useStyles = makeStyles((theme) => ({
  '@global': {
    body: {
      backgroundColor: theme.palette.primary.light,
    },
  },
  card: {
    backgroundColor: theme.palette.background.paper,
    marginTop: theme.spacing(8),
    padding: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    borderRadius: theme.shape.borderRadius,
  },
}));

function RegisterPage({ setAuth, ...props }) {
  function handleSubmit(event) {
    event.preventDefault();

    // Get user inputs (TODO:)
    const name = event.target[0].value;
    const handle = event.target[2].value;
    const password = event.target[4].value;

    // Quick validation
    if (!handle || !password) return;

    // Send to backend
    Axios.post(`${url}/auth/register`, { name, handle, password })
      .then((response) => {
        console.log(response);
        const data = response.data;
        setAuth(data);
        props.history.push('/');
      })
      .catch((err) => {
        console.error(err);
        toast.error(DEFAULT_ERROR_TEXT);
      });
  }

  const classes = useStyles();

  return (
    <Container component="main" maxWidth="sm">
      <Box boxShadow={3} className={classes.card}>
        <Avatar>
          <DeveloperOutlinedIcon color="secondary" />
        </Avatar>
        <Typography component="h1" variant="h5">
          Register
        </Typography>
        <form noValidate onSubmit={handleSubmit}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="name_first"
            label="Firstname"
            name="name_first"
            type="text"
            autoFocus
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="name_last"
            label="Lastname"
            name="name_last"
            type="text"
            autoFocus
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email"
            name="email"
            type="email"
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <Button type="submit" fullWidth variant="contained" color="primary">
            Sign Up
          </Button>
          <Grid container>
            <Grid item>
              <br />
              <Link href="/login" variant="body1">
                {'Already have an account? Login'}
              </Link>
            </Grid>
          </Grid>
        </form>
      </Box>
    </Container>
  );
}

export default RegisterPage;
