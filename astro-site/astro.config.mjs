// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightClientMermaid from '@pasqal-io/starlight-client-mermaid';

export default defineConfig({
	site: 'https://docs.superheld.app',
	integrations: [
		starlight({
			title: 'superheld.app',
			defaultLocale: 'root',
			locales: {
				root: { label: 'Deutsch', lang: 'de' },
			},
			logo: {
				light: './src/assets/logo.svg',
				dark: './src/assets/logo-dark.svg',
			},
			lastUpdated: true,
			plugins: [starlightClientMermaid()],
			sidebar: [
				{
					label: 'Erste Schritte',
					autogenerate: { directory: 'getting-started' },
				},
				{
					label: 'Für Experten',
					autogenerate: { directory: 'experts' },
				},
			],
			head: [
				{ tag: 'meta', attrs: { property: 'og:image', content: '/images/og-image.png' } },
				{ tag: 'link', attrs: { rel: 'manifest', href: '/site.webmanifest' } },
				{ tag: 'link', attrs: { rel: 'apple-touch-icon', href: '/apple-touch-icon.png' } },
				{ tag: 'link', attrs: { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' } },
				{ tag: 'link', attrs: { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png' } },
				{ tag: 'link', attrs: { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png' } },
			],
			customCss: ['./src/styles/custom.css'],
		}),
	],
});
