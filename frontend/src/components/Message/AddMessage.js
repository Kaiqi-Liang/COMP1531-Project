import axios from 'axios';
import {
  Button,
  TextField,
  InputAdornment,
  IconButton,
} from '@material-ui/core';
import React from 'react';
import SendIcon from '@material-ui/icons/Send';
import TimerIcon from '@material-ui/icons/Timer';
import { makeStyles } from '@material-ui/styles';
import AuthContext from '../../AuthContext';
import AddMessageTimerDialog from './AddMessageTimerDialog';

const useStyles = makeStyles((theme) => ({
  flex: {
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
  },
  input: {
    margin: theme.spacing(1),
    marginRight: 0,
  },
  button: {
    margin: theme.spacing(1),
    marginLeft: 0,
    alignSelf: 'stretch',
  },
  rightIcon: {
    marginLeft: theme.spacing(1),
  },
}));

const TIMER_INACTIVE_VALUE = -1;

function AddMessage({ channel_id = '', onAdd = () => {} }) {
  const classes = useStyles();
  const [currentMessage, setCurrentMessage] = React.useState('');
  const [currentTimer, setCurrentTimer] = React.useState(TIMER_INACTIVE_VALUE);
  const [timerDialogOpen, setTimerDialogOpen] = React.useState(false);
  const token = React.useContext(AuthContext);

  const isTimerSet = currentTimer !== TIMER_INACTIVE_VALUE;

  const submitMessage = () => {
    const message = currentMessage.trim();
    if (!message) return;
    setCurrentMessage('');

    // Depending on if timer active
    if (isTimerSet) {
      axios.post(`/message/sendlater`, {
        token,
        channel_id,
        message,
        time_sent: (currentTimer.getTime() / 1000), // ms to s conversion
      })
        .then(({ data }) => {
          console.log(data);
        })
        .catch((err) => {});
      setCurrentTimer(TIMER_INACTIVE_VALUE);
    } else {
      if (message == '/standup') {
        alert('Hello. This feature isn\'t finished yet. We won\'t be expecting you to demonstrate this on the frontend in iteration 2'); // TODO
      }
      axios.post(`/message/send`, {
        token,
        channel_id,
        message,
      })
        .then(({ data }) => {
          console.log(data);
          onAdd();
        })
        .catch((err) => {});
    }
  };

  const keyDown = (e) => {
    if (e.key === 'Enter' && !e.getModifierState('Shift')) {
      e.preventDefault();
      submitMessage();
    }
  };

  return (
    <>
      <div className={classes.flex}>
        <TextField
          className={classes.input}
          label="Send a message 💬"
          multiline
          placeholder="..."
          // helperText="Add a new message to this channel!"
          fullWidth
          margin="normal"
          variant="filled"
          onKeyDown={keyDown}
          value={currentMessage}
          onChange={(e) => setCurrentMessage(e.target.value)}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton
                  aria-label="toggle visibility"
                  onClick={() =>
                    isTimerSet ? setCurrentTimer(-1) : setTimerDialogOpen(true)
                  }
                >
                  <TimerIcon color={isTimerSet ? 'secondary' : undefined} />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
        <Button
          className={classes.button}
          variant="contained"
          color="primary"
          onClick={submitMessage}
        >
          Send
          <SendIcon className={classes.rightIcon} />
        </Button>
      </div>
      <AddMessageTimerDialog
        open={timerDialogOpen}
        handleClose={() => setTimerDialogOpen(false)}
        onTimerChange={setCurrentTimer}
      />
    </>
  );
}

export default AddMessage;
