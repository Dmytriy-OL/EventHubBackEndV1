import Header from './Header';

export default {
  title: 'Components/Header',
  component: Header,
  argTypes: {
    title: { control: 'text' },
    showLogo: { control: 'boolean' }
  },
};

const HeaderTemplate = (args) => <Header {...args} />;

export const Default = HeaderTemplate.bind({});
Default.args = { title: 'Welcome', showLogo: true };

export const NoLogo = HeaderTemplate.bind({});
NoLogo.args = { title: 'Welcome', showLogo: false };

export const CustomTitle = HeaderTemplate.bind({});
CustomTitle.args = { title: 'Hello, User!', showLogo: true };
