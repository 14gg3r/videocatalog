document.querySelector('.js-menu-icon')?.addEventListener('click', function () {
    document.querySelector('.side-menu').classList.toggle('open');
    document.querySelector('.js-menu-icon').classList.toggle('open');
})

function getTableItems(items) {
    let itemsHtml = ``

    items.map(item => {
        const {
            catalogNumber,
            performer,
            title,
            duration,
            video_type,
            director,
            screenwriter,
            composer,
            year,
            youtube_link,
            rutube_link,
            yandex_link,
            vk_link,
            zen_link,
            upc,
            files,

        } = item
        itemsHtml += `
        <tr>
<td>${catalogNumber}</td>
<td>${performer}</td>
<td>${title}</td>
<td>${duration}</td>
<td>${video_type}</td>
<td>${director}</td>
<td>${screenwriter}</td>
<td>${composer}</td>
<td>${year}</td>
<td>
   ${youtube_link ? `<a target="_blank" href="${youtube_link}">Ссылка</a>` : '-'}   
</td>
<td>
   ${rutube_link ? `<a target="_blank" href="${rutube_link}">Ссылка</a>` : '-'}   
</td>
<td>
   ${yandex_link ? `<a target="_blank" href="${yandex_link}">Ссылка</a>` : '-'}   
</td>
<td>
   ${vk_link ? `<a target="_blank" href="${vk_link}">Ссылка</a>` : '-'}   
</td>
<td>
   ${zen_link ? `<a target="_blank" href="${zen_link}">Ссылка</a>` : '-'}   
</td>


<td>${upc}</td>

<td>
   ${files ? `<a href="${files}">Файл</a>` : '-'}   
</td>

</tr>
        `
    })

    return itemsHtml
}


document.querySelector('.js-search-input')?.addEventListener('input', function (e) {
    const {value} = e.target;
    const table = document.querySelector('.js-search-table tbody');

    const foundItems = items.filter(item => {
        const {
            performer,
            title,
            upc,
            catalogNumber,
            duration,
            video_type,
            director,
            screenwriter,
            composer,
            year,
            youtube_link,
            rutube_link,
            yandex_link,
            vk_link,
            zen_link,
            files,
        } = item
        const cleanedValue = value.trim().toLowerCase()
        return files.toLowerCase().includes(cleanedValue)
            || performer.toLowerCase().includes(cleanedValue)
            || title.toLowerCase().includes(cleanedValue)
            || upc.toLowerCase().includes(cleanedValue)
            || catalogNumber.toLowerCase().includes(cleanedValue)
            || duration.toLowerCase().includes(cleanedValue)
            || video_type.toLowerCase().includes(cleanedValue)
            || director.toLowerCase().includes(cleanedValue)
            || screenwriter.toLowerCase().includes(cleanedValue)
            || composer.toLowerCase().includes(cleanedValue)
            || year.toLowerCase().includes(cleanedValue)
            || youtube_link.toLowerCase().includes(cleanedValue)
            || rutube_link.toLowerCase().includes(cleanedValue)
            || yandex_link.toLowerCase().includes(cleanedValue)
            || vk_link.toLowerCase().includes(cleanedValue)
            || zen_link.toLowerCase().includes(cleanedValue)
    });


    table.innerHTML = getTableItems(foundItems);
})


document.querySelector('.js-cross')?.addEventListener('click', function (e) {
    document.querySelector('.js-modal')?.classList.toggle('close');
})

document.querySelector('.js-search-cross')?.addEventListener('click', function (e) {
    document.querySelector('.js-search-input').value = ''

    const table = document.querySelector('.js-search-table tbody');
    table.innerHTML = getTableItems(items);

})


const inputWrappers = document.querySelectorAll('form p')

inputWrappers.forEach(wrapper => {
    wrapper.innerHTML = wrapper.innerHTML + '<span class="input-cross js-input-cross">×</span>'

    wrapper.querySelector('.js-input-cross').addEventListener('click', (e) => {
        e.target.parentNode.querySelector('input').value = ''
    });

})

function loadFromLocalstorage(form) {
    const inputs = form.querySelectorAll('input');

    [...inputs].forEach(input => {
        const value = localStorage.getItem(input.id);
        if (value) {
            input.value = JSON.parse(value);
        }
    })
}

function saveToLocalstorage(form) {
    const inputs = form.querySelectorAll('input');

    [...inputs].forEach(input => {
        if (input.type === 'text' || input.type === 'number' || input.type === 'url') {

            input.addEventListener('input', (e) => {
                localStorage.setItem(input.id, JSON.stringify(input.value));
            })
        }
    })
}

function cleanLocalstorage(form) {
    const inputs = form.querySelectorAll('input');

    [...inputs].forEach(input => {
        if (input.type === 'text' || input.type === 'number' || input.type === 'url') {
            localStorage.setItem(input.id, null);
        }
    })
}

function initSaveToLocalstorageForm(form) {
    if (!form) {
        return null
    }

    loadFromLocalstorage(form)
    saveToLocalstorage(form)


    form.addEventListener('submit', (e) => {
        cleanLocalstorage(form)
    })
}


document.addEventListener("DOMContentLoaded", (event) => {
    const form = document.querySelector('.js-adding-form');

    initSaveToLocalstorageForm(form)

});
