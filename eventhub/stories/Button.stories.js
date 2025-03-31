import { createButton } from './Button';

export default {
  title: 'Components/Button',
  component: createButton,
  argTypes: {
    label: { control: 'text' },
    size: { control: { type: 'select', options: ['small', 'medium', 'large'] } },
    primary: { control: 'boolean' }
  },
};

const Template = (args) => createButton(args);

export const Primary = Template.bind({});
Primary.args = { label: 'Primary Button', size: 'medium', primary: true };
