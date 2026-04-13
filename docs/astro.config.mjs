// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	trailingSlash: 'always',
	build: { format: 'directory' },
	integrations: [
		starlight({
			title: 'AgentOS SDK',
			sidebar: [
				{ label: 'Principles', slug: 'principles' },
				{ label: 'Shapes', slug: 'shapes' },
				{ label: 'Skills', slug: 'skills' },
				{ label: 'LLM', slug: 'llm' },
				{ label: 'Connections', slug: 'connections' },
				{ label: 'Auth flows', slug: 'auth-flows' },
				{ label: 'Data', slug: 'data' },
				{
					label: 'Reverse engineering',
					items: [
						{ label: 'Overview', slug: 'reverse-engineering/overview' },
						{ label: '1. Transport', slug: 'reverse-engineering/1-transport' },
						{ label: '2. Discovery', slug: 'reverse-engineering/2-discovery' },
						{ label: '3. Auth', slug: 'reverse-engineering/3-auth' },
						{ label: '3. Auth — NextAuth', slug: 'reverse-engineering/3-auth-nextauth' },
						{ label: '3. Auth — WorkOS', slug: 'reverse-engineering/3-auth-workos' },
						{ label: '3. Auth — macOS Keychain', slug: 'reverse-engineering/3-auth-macos-keychain' },
						{ label: '4. Content', slug: 'reverse-engineering/4-content' },
						{ label: '5. Social', slug: 'reverse-engineering/5-social' },
						{ label: '6. Desktop apps', slug: 'reverse-engineering/6-desktop-apps' },
						{ label: '6. Desktop apps — Electron', slug: 'reverse-engineering/6-desktop-apps-electron' },
						{ label: '7. MCP', slug: 'reverse-engineering/7-mcp' },
					],
				},
			],
		}),
	],
});
