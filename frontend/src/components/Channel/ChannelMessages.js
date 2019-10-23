import React from 'react';
import axios from 'axios';

import { List, ListSubheader } from '@material-ui/core';
import { pollingInterval, getIsPolling, subscribeToStep, unsubscribeToStep } from '../../utils/update';
import Message from '../Message';
import AuthContext from '../../AuthContext';
import { toast } from 'react-toastify';
import { CHANNEL_ERROR_TEXT } from '../../utils/text';
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
    const { messages, start, end } = data;
    setCurrentStart(end); // TODO: add/remove problems
    setMessages(messages);
  })
  .catch((err) => {
    console.error(err);
    toast.error(CHANNEL_ERROR_TEXT);
  });

  React.useEffect(() => {
    fetchChannelMessages();
    subscribeToStep(fetchChannelMessages);
    return () => unsubscribeToStep(fetchChannelMessages);
  }, [channel_id])

  useInterval(() => {
    if (getIsPolling()) fetchChannelMessages();
  }, pollingInterval);

  return (
    <>
      <List
        subheader={<ListSubheader>Messages</ListSubheader>}
        style={{ width: '100%' }}
      >
        {messages.slice().reverse().map((message) => (
          <Message {...message} />
        ))}
      </List>
      <AddMessage channel_id={channel_id} />
    </>
  );
}

export default ChannelMessages;
