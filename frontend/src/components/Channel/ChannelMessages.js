import React from 'react';
import axios from 'axios';

<<<<<<< HEAD
import { List, ListSubheader } from '@material-ui/core';
=======
import { List, ListSubheader, Button } from '@material-ui/core';
>>>>>>> 760cab0852d04714f96583f53649d5895803ed06
import { pollingInterval, getIsPolling, subscribeToStep, unsubscribeToStep } from '../../utils/update';
import Message from '../Message';
import AuthContext from '../../AuthContext';
import AddMessage from '../Message/AddMessage';
import { useInterval } from '../../utils';

function ChannelMessages({ channel_id = '' }) {
  const [messages, setMessages] = React.useState([]);
  const [currentStart, setCurrentStart] = React.useState(0);
  const token = React.useContext(AuthContext);

  const fetchChannelMessages = () => axios
  .get('/channel/messages', {
    params: {
      token,
      channel_id,
      start: currentStart,
    },
  })
  .then(({ data }) => {
    const { messages: newMessages, start, end } = data;
    setCurrentStart(end); // TODO: add/remove problems
    setMessages(messages.concat(newMessages));
  })
  .catch((err) => {});

  const resetChannelMessages = () => axios
  .get('/channel/messages', {
    params: {
      token,
      channel_id,
      start: 0,
    },
  })
  .then(({ data }) => {
    const { messages: newMessages, start, end } = data;
    setCurrentStart(end); // TODO: add/remove problems
    setMessages(newMessages);
  })
  .catch((err) => {});

  React.useEffect(() => {
    resetChannelMessages();
    subscribeToStep(fetchChannelMessages);
    return () => unsubscribeToStep(fetchChannelMessages);
  }, [channel_id])

  return (
    <>
      <hr />
      {
        (currentStart != -1 &&
          <Button
            variant="outlined"
            color="secondary"
            onClick={() => fetchChannelMessages()}
          >
            Previous messages
          </Button>
        )
      }
      <List
        subheader={<ListSubheader>Messages</ListSubheader>}
        style={{ width: '100%' }}
      >
        {messages.slice().reverse().map((message) => (
<<<<<<< HEAD
          <Message {...message} />
=======
          <Message key={message.message_id} {...message} />
>>>>>>> 760cab0852d04714f96583f53649d5895803ed06
        ))}
      </List>
      <AddMessage onAdd={resetChannelMessages} channel_id={channel_id} />
    </>
  );
}

export default ChannelMessages;
