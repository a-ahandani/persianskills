import {continueRender, delayRender, staticFile} from 'remotion';

/* Load Sahel before the first frame. A missing Persian font is the most common
   silent failure: Chrome falls back to a system font and nobody notices until review. */
const handle = delayRender('Loading Sahel');
const face = new FontFace('Sahel', `url(${staticFile('fonts/Sahel-VF.woff2')}) format('woff2')`, {weight: '400 900'});
face
	.load()
	.then((f) => {
		document.fonts.add(f);
		continueRender(handle);
	})
	.catch((err) => {
		console.error('Sahel failed to load', err);
		continueRender(handle);
	});

export const FA = '"Sahel", Tahoma, sans-serif';
export const MONO = 'ui-monospace, "SF Mono", Menlo, monospace';
